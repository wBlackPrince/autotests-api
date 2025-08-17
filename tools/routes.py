from enum import Enum


class ApiRoutes(str, Enum):
    USERS = "/api/v1/users"
    FILES = "/api/v1/files"
    EXERCISES = "api/v1/exercises"
    COURSES = "/api/v1/courses"
    AUTHENTIFICATION = "/api/v1/authentication"

    def __str__(self):
        return self.value