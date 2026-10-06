# __ini__.py 파일 (초기화 파일)
# 패키지를 로드할 때 실행되는 초기화 파일

# 1. 패키지를 import 할 떄 실행되어야하는 초기화
print("__init__")

# 2. 패키지 메타데이터
version = "1.0.0"

# 패키지 re-export
# from mypackage.mymath import add # 절대 import
from .mymath import add, PI # 상대 import