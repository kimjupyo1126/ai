'''
sample_pac/ab/__init__.py
as 패키지를 import 할 때 자동 실행
form sample_pac.ab import *을 수행시 a모듈만 자동 impor되도록 하기 위해
'''
__all__ = ['a']
print('sample_pac.ab 패키지 로드')