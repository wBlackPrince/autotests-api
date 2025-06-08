import grpc
import course_service_pb2_grpc
import course_service_pb2
from concurrent import futures

import user_service_pb2_grpc


class CourseServiceService(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        print(f'Запрошена информации о курсе с идентификатором {request.course_id}')
        return course_service_pb2.GetCourseResponse(course_id = request.course_id,
                                                    title = "Автотесты API",
                                                    description = "Будем изучать написание API автотестов")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 12))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC сервер запущен на порте 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
