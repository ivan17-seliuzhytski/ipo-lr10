import requests

def fetch_popular_repositories():
    url = "https://api.github.com/search/repositories?q=stars:>10000&sort=stars&order=desc"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")
        return []

def display_repositories(repositories):
    for idx, repo in enumerate(repositories[:10], start=1):  # Получаем топ-10 репозиториев
        name = repo['full_name']
        stars = repo['stargazers_count']
        print(f"{idx}. Repository: {name}; Stars: {stars:,};")

def main():
    repositories = fetch_popular_repositories()
    display_repositories(repositories)

if __name__ == "__main__":
    main()
