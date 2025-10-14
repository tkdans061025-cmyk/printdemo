echo "내용" > README.md    # 파일 만들기
git add README.md          # 스테이지에 추가
git commit -m "첫 커밋"    # 첫 커밋 생성


print("hello world")
# main_print_v2
# 변수와 함께 출력
name = "홍길동"
age = 20
print("이름:", name, "나이:", age)

# 포맷 문자열 (f-string)
print(f"{name}은 {age}살입니다.")

# 여러 줄 출력
print("""
안녕하세요!
파이썬 기초 실습 중입니다.
열심히 해봅시다!
""")

# sep과 end 사용
print("Python", "is", "fun", sep="-", end="! 🚀\n")

# 리스트 출력
fruits = ["사과", "바나나", "체리"]
print("과일 목록:", fruits)

# 딕셔너리 출력
person = {"name": "철수", "city": "서울"}
print("사람 정보:", person)

# rich 모듈 사용 (설치 필요: pip install rich)
from rich.console import Console
from rich.table import Table
from rich import print as rprint

# rich로 스타일리시한 출력
console = Console()

rprint("[bold red]Rich 모듈로 출력하기[/bold red]")
rprint("[blue]이것은 파란색 텍스트입니다[/blue]")
rprint("[green on yellow]초록색 글자에 노란색 배경[/green on yellow]")

# 테이블 만들기
table = Table(title="학생 정보")
table.add_column("이름", style="cyan")
table.add_column("나이", style="magenta")
table.add_column("전공", style="green")

table.add_row("김철수", "22", "컴퓨터공학")
table.add_row("이영희", "21", "기계공학")
table.add_row("박민수", "23", "전자공학")

console.print(table)

# 프로그래스 바 (추가 실습)
from rich.progress import track
import time

print("작업 진행 중...")
for i in track(range(10), description="처리 중..."):
    time.sleep(0.5)

print("모든 작업 완료!")