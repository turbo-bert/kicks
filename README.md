open cmd

    curl -o p.exe -L https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

    p.exe PrependPath=1 /passive

cmd reopen

    pip install kicks

    python -m kicks
