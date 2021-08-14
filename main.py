import flask
import requests

app = flask.Flask(__name__)


@app.route('/api/supervisors', methods=['GET'])
def get_supervisors():
    url = "https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers"
    supervisor_data = requests.get(url).json()

    # sorting code
    sorted_list = []
    for i in range(0, len(supervisor_data)):
        supervisor = supervisor_data[i]
        if not supervisor['jurisdiction'].isnumeric():  # omit numerical jurisdictions
            jurisdiction, last_name, first_name = [supervisor[key] for key in ('jurisdiction', 'lastName', 'firstName')]
            # make an id with the relevant letters (first of jurisdiction, first of last name, and first of first name).
            # Append the index at end for retrieving data later.
            sorting_id = jurisdiction[0] + last_name[0] + first_name[0] + '-' + str(i)
            sorted_list.append(sorting_id)
    sorted_list = sorted(sorted_list)  # sort list

    # fill in the information based on the index in the sorting id
    response = []
    for sorting_id in sorted_list:
        supervisor_index = int(sorting_id.split('-')[-1])  # extract the index
        supervisor = supervisor_data[supervisor_index]
        formatted_sting = f"{supervisor['jurisdiction']} - {supervisor['lastName']}, {supervisor['firstName']}"
        response.append(formatted_sting)

    return {'supervisors': response}


@app.route('/api/submit', methods=['POST'])
def submit():
    req_fields = ['firstName', 'lastName', 'superVisor']
    form = flask.request.form
    errors = []

    [errors.append(f'Missing {field}') for field in req_fields if field not in form]  # find missing required fields

    if len(errors) > 0:  # error response
        response = flask.jsonify({'errors': errors, 'success': False})
        response.status_code = 400
    else:  # success response
        print("\n--Success!--\n")
        for field, value in form.items():
            print(f"{field}: {value}")
        print("\n--End of Output--\n")
        response = flask.jsonify(success=True)

    return response


app.run(host="0.0.0.0")
