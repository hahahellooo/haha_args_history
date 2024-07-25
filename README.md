# haha_args_history
- parquet 파일의 정보를 cli 기반으로 조회

### 사용법
```
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```

### Dev env setting 
```
$ git clone <URL>
$ cd <PJT_NAME>
$ pyenv virtualenv 3.11.9 clean 
$ pyenv global clean 
$ rm -rf .venv
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pdm list
$ pytest

pytest
================================================= test session starts ==================================================
platform linux -- Python 3.11.9, pytest-8.3.1, pluggy-1.5.0
rootdir: /home/hahahellooo/code/haha_args_history
configfile: pyproject.toml
plugins: cov-5.0.0
collected 0 items


# option
$ pdm init
$ pdm venv create
$ source .venv/bin/activate
$ pdm add -dG test pytest pytest-cov
$ pytest
```

### deploy
```bash
# dev branch
pip install git+https://github.com/hahahellooo/haha_args_history.git@0.2.0/args

# main branch
pip install git+https://github.com/hahahellooo/haha_args_history.git@main
```

### Ref
-  https://pdm-project.org/en/latest/usage/dependency/#add-development-only-dependencies
