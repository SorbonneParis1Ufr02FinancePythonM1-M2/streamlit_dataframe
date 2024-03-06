import repository
import view


def main():
    data = repository.get_data()
    view.to_streamlit(data)


if __name__ == "__main__":
    main()
