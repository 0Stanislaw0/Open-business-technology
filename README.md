### Выполнение тестового задания https://docs.google.com/document/d/1Sxnc0U674KMghAGKyrPcs8FZokm-Wg_APWFAILQte4g/edit

### Установка
  1. Установите и активируйте виртуальное окружение

    virtualenv --python=python3.6 ./test_venv
    source ./test_venv/bin/activate
      
  2. Установите пакет
  
    pip install m3-0.1.1.tar.gz \
    --extra-index-url http://pypi.bars-open.ru/simple/ \
    --trusted-host pypi.bars-open.ru
    
  3. Запустите сервер
  
    python ./test_venv/lib/python3.6/site-packages/m3_project/manage.py runserver 0.0.0.0:8000
  
  4. PROFIT!!!
