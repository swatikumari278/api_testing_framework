
class UserAPI:

    def __init__(self,request_context):
        self.request_context = request_context

    def get_user_by_id(self, user_id):
        return self.request_context.get(f"/users/{user_id}")

    def get_all_users(self):
        return  self.request_context.get("/users")

    def create_user(self,payload):
        return self.request_context.post("/users",data=payload)

    def update_user(self, user_id, payload):
        return self.request_context.put(f"/users/{user_id}", data=payload)

    def delete_user(self, user_id):
        return self.request_context.delete(f"/users/{user_id}")


