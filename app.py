from flask import Flask, jsonify, request

app = Flask(__name__)

courses = [
    {"id" : 1, "title" : "DevOps Engineering", "instructor" : "Memoona Amjad"},
    {"id" : 2, "title" : "Software Design", "instructor" : "Dr. Adnan Shah"}
]

@app.route(route="/courses", methods = ['GET'] )
def get_students():
    return jsonify(courses)

@app.route(route="/courses/<int: course_id>", methods = ['POST'])
def get_course_by_ID(course_id):
    data = [ {"id" : len(courses), 
              "title" : "title",
              "instructor" : "instructor"}]
    
    course = next((c for c in courses["id"] == course_id), None)

    if(course):
        data.get_json({"title": data["title"], "instructor": data["instructor"]})
        return jsonify(courses), 400


@app.route(route="/courses/<int:course_id>", methods = ['GET'])
def update_course(course_id):
    course = next((c for c in courses["id"] == course_id), None)
    if(course):
        return jsonify(course), 201

@app.route(route="/courses", methods = ["PUT"])
def put_course():
    data = [ {"id" : len(courses), 
              "title" : "title",
              "instructor" : "instructor"}]
    return jsonify(data), 202

@app.route(route="/courses/<int: course_id>", methods = ['DELETE'])
def delete_course(course_id):
    data = {c for c in courses["id"] != course_id}
    return jsonify(data)

__app__ = '__main__'
debug =True
    