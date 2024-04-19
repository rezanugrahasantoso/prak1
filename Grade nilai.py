nilai = int(input('Berapa nilai Anda? '))

if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B+'
elif nilai >= 70:
    grade = 'B'
elif nilai >= 60:
    grade = 'C'
elif nilai >= 50:
    grade = 'D'
else:
    grade = 'E'

print(f'Grade: {grade}')
