from locust import HttpUser, task

class ReminderUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")
