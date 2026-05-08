from api.user_api import UserAPI

def test_get_user_by_id(api_request_context):
    user_api = UserAPI(api_request_context)

    response = user_api.get_user_by_id(1)
    body = response.json()

    assert response.status == 200
    assert  body["name"] == "Leanne Graham"
    assert  body["id"] == 1


def test_get_all_users(api_request_context):
    user_api = UserAPI(api_request_context)

    reponse = user_api.get_all_users()

    body = reponse.json()

    assert  reponse.status == 200
    assert len(body) > 0


def test_create_user(api_request_context):
    user_api = UserAPI(api_request_context)

    payload ={
        "name" : "swati",
        "username" : "swatiqa",
        "email":"swati@test.com"
    }

    response = user_api.create_user(payload)
    body = response.json()

    assert response.status == 201
    assert  body["name"]=="swati"
    assert body["username"] =="swatiqa"


def test_update_user(api_request_context):
    user_api = UserAPI(api_request_context)

    payload ={
        "name" : "swati_updated",
        "username" : "swatiqa_updated",
        "eamil" : "swati@test.com"
    }

    response = user_api.update_user(1,payload)
    body = response.json()

    assert response.status == 200
    assert body["name"] == "swati_updated"
    assert body["username"] == "swatiqa_updated"



def test_delete_user(api_request_context):
    user_api = UserAPI(api_request_context)
    response = user_api.delete_user(1)

    assert response.status == 200