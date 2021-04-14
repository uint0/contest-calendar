import flask
import providers
import ical

app = flask.Flask(__name__)


@app.route('/calendar/<site>')
def get_site_calendar(site):
    if not providers.has_provider(site):
        return f"Could not find records for site. Valid sites are: {','.join(providers.list_providers())}", 404, {'Content-Type': 'text/plain'}
    
    calendar = ical.make_ical(site)
    # TODO: can we get hacked?
    return str(calendar), 200, {'Content-Type': 'text/calendar', 'Content-Disposition': f'attachment; filename={site}.ics'}


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
