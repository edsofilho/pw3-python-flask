from flask import Blueprint, render_template, request, url_for, redirect
import requests


main = Blueprint('main', __name__)
API_BASE_URL = "https://rickandmortyapi.com/api"


def fetch_api(endpoint: str, params: dict | None = None):
	try:
		response = requests.get(f"{API_BASE_URL}{endpoint}", params=params, timeout=10)
		response.raise_for_status()
		return response.json(), None
	except requests.HTTPError as http_error:
		status_code = http_error.response.status_code if http_error.response is not None else None
		if status_code == 404:
			return None, "Recurso não encontrado."
		return None, f"Erro na API: {status_code}"
	except requests.RequestException:
		return None, "Não foi possível conectar à API."


@main.route('/')
def index():
	return render_template('index.html')


@main.route('/characters')
def characters():
	name_query = (request.args.get('name') or '').strip()
	try:
		page = int(request.args.get('page', 1))
	except (TypeError, ValueError):
		page = 1

	params: dict = {'page': page}
	if name_query:
		params['name'] = name_query

	data, error = fetch_api('/character', params=params)
	if error:
		return render_template(
			'characters.html',
			error=error,
			characters=[],
			info=None,
			name=name_query,
			page=page,
		)

	characters_list = data.get('results', []) if isinstance(data, dict) else []
	info = data.get('info', {}) if isinstance(data, dict) else {}
	prev_page = page - 1 if info.get('prev') else None
	next_page = page + 1 if info.get('next') else None

	return render_template(
		'characters.html',
		characters=characters_list,
		info=info,
		name=name_query,
		page=page,
		prev_page=prev_page,
		next_page=next_page,
	)


@main.route('/characters/<int:character_id>')
def character_detail(character_id: int):
	data, error = fetch_api(f"/character/{character_id}")
	if error:
		return render_template('character_detail.html', error=error, character=None)

	character = data if isinstance(data, dict) else None
	return render_template('character_detail.html', character=character)

