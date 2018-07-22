from conduit.app import create_table,create_app

def main():
    # create_table() ## fro testing issue
    app = create_app()
    app.run()

if __name__ == '__main__':
    main()