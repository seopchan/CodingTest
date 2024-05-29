# 1. 전공평점 3.3 이상   
# 전공평점 : 전공과목별(학점 * 과목평점)의 합 / 학점의 총합
# P는 계산 제외


GRADE_SCORE = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

scores = []
credits = []
for _ in range(20):
    subject, credit, grade = input().split()
    if grade != "P":
        credits.append(float(credit))
        scores.append(credits[-1] * GRADE_SCORE[grade])

print(f"{sum(scores) / sum(credits):.6f}")