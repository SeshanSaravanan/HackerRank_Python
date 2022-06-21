 if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    marks=0
    for i in student_marks[query_name]:
        marks=marks+i
    avg=marks/3
    print("%.2f"%avg)
