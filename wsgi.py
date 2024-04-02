from app import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6699, ssl_context=('xiaomingya.com.pem', 'xiaomingya.com.key'))