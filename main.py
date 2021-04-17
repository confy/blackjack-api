from webapp import create_app

if __name__ == '__main__':
    """ Creates and Runs flask app """
    app = create_app()
    app.run(debug=True)
