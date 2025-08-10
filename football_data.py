import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from bs4.element import Tag
import random
import os


epl_club_urls = [
    # EPL teams links
    # "https://www.transfermarkt.com/arsenal-fc/kader/verein/11",
    # "https://www.transfermarkt.com/aston-villa/kader/verein/405",
    # "https://www.transfermarkt.com/afc-bournemouth/kader/verein/989",
    # "https://www.transfermarkt.com/brentford-fc/kader/verein/1148",
    # "https://www.transfermarkt.com/brighton-hove-albion/kader/verein/1237",
    # "https://www.transfermarkt.com/burnley-fc/kader/verein/1132",
    # "https://www.transfermarkt.com/chelsea-fc/kader/verein/631",
    # "https://www.transfermarkt.com/crystal-palace/kader/verein/873",
    # "https://www.transfermarkt.com/everton-fc/kader/verein/29",
    # "https://www.transfermarkt.com/fulham-fc/kader/verein/931",
    # "https://www.transfermarkt.com/liverpool-fc/kader/verein/31",
    # "https://www.transfermarkt.com/luton-town/kader/verein/1031",
    # "https://www.transfermarkt.com/manchester-city/kader/verein/281",
    "https://www.transfermarkt.com/manchester-united/kader/verein/985",
    # "https://www.transfermarkt.com/newcastle-united/kader/verein/762",
    # "https://www.transfermarkt.com/nottingham-forest/kader/verein/703",
    # "https://www.transfermarkt.com/sheffield-united/kader/verein/350",
    # "https://www.transfermarkt.com/tottenham-hotspur/kader/verein/148",
    # "https://www.transfermarkt.com/west-ham-united/kader/verein/379",
    # "https://www.transfermarkt.com/wolverhampton-wanderers/kader/verein/543",
    # 'https://www.transfermarkt.com/southampton-fc/startseite/verein/180',
    # 'https://www.transfermarkt.com/ipswich-town/startseite/verein/677',
    # 'https://www.transfermarkt.com/leicester-city/startseite/verein/1003'


    # Laliga teams links
    # "https://www.transfermarkt.com/real-madrid/startseite/verein/418",
    # "https://www.transfermarkt.com/fc-barcelona/startseite/verein/131",
    # "https://www.transfermarkt.com/atletico-madrid/startseite/verein/13",
    # "https://www.transfermarkt.com/real-sociedad-san-sebastian/startseite/verein/681",
    # "https://www.transfermarkt.com/real-betis-sevilla/startseite/verein/150",
    # "https://www.transfermarkt.com/fc-sevilla/startseite/verein/368",
    # "https://www.transfermarkt.com/ca-osasuna/startseite/verein/331",
    # "https://www.transfermarkt.com/athletic-bilbao/startseite/verein/621",
    # "https://www.transfermarkt.com/deportivo-alaves/startseite/verein/1108",
    # "https://www.transfermarkt.com/celta-vigo/startseite/verein/940",
    # "https://www.transfermarkt.com/fc-valencia/startseite/verein/1049",
    # "https://www.transfermarkt.com/fc-villarreal/startseite/verein/1050",
    # "https://www.transfermarkt.com/fc-getafe/startseite/verein/3709",
    # "https://www.transfermarkt.com/rayo-vallecano/startseite/verein/367",
    # "https://www.transfermarkt.com/rcd-mallorca/startseite/verein/237",
    # "https://www.transfermarkt.com/ud-las-palmas/startseite/verein/472",
    # "https://www.transfermarkt.com/fc-girona/startseite/verein/12321",
    # "https://www.transfermarkt.com/real-valladolid/startseite/verein/366",
    # "https://www.transfermarkt.com/cd-leganes/startseite/verein/1244",
    # "https://www.transfermarkt.com/espanyol-barcelona/startseite/verein/714"


    # Bundesliga teams link
    # "https://www.transfermarkt.com/bayer-04-leverkusen/startseite/verein/15",
    # "https://www.transfermarkt.com/vfb-stuttgart/startseite/verein/79",
    # "https://www.transfermarkt.com/fc-bayern-munchen/startseite/verein/27",
    # "https://www.transfermarkt.com/rasenballsport-leipzig/startseite/verein/23826",
    # "https://www.transfermarkt.com/borussia-dortmund/startseite/verein/16",
    # "https://www.transfermarkt.com/eintracht-frankfurt/startseite/verein/24",
    # "https://www.transfermarkt.com/tsg-1899-hoffenheim/startseite/verein/533",
    # "https://www.transfermarkt.com/sv-werder-bremen/startseite/verein/86",
    # "https://www.transfermarkt.com/sc-freiburg/startseite/verein/60",
    # "https://www.transfermarkt.com/fc-augsburg/startseite/verein/167",
    # "https://www.transfermarkt.com/vfl-wolfsburg/startseite/verein/82",
    # "https://www.transfermarkt.com/1-fsv-mainz-05/startseite/verein/39",
    # "https://www.transfermarkt.com/borussia-monchengladbach/startseite/verein/18",
    # "https://www.transfermarkt.com/1-fc-union-berlin/startseite/verein/89",
    # "https://www.transfermarkt.com/vfl-bochum/startseite/verein/80",
    # "https://www.transfermarkt.com/fc-st-pauli/startseite/verein/35",
    # "https://www.transfermarkt.com/holstein-kiel/startseite/verein/269"
    # "https://www.transfermarkt.com/1-fc-heidenheim-1846/startseite/verein/2036"


    # League 1 teams links
    # "https://www.transfermarkt.com/paris-saint-germain/startseite/verein/583",
    # "https://www.transfermarkt.com/as-monaco/startseite/verein/162",
    # "https://www.transfermarkt.com/stade-brestois-29/startseite/verein/3911",
    # "https://www.transfermarkt.com/losc-lille/startseite/verein/1082",
    # "https://www.transfermarkt.com/ogc-nizza/startseite/verein/417",
    # "https://www.transfermarkt.com/olympique-lyon/startseite/verein/1041",
    # "https://www.transfermarkt.com/rc-lens/startseite/verein/826",
    # "https://www.transfermarkt.com/olympique-marseille/startseite/verein/244",
    # "https://www.transfermarkt.com/stade-reims/startseite/verein/1421",
    # "https://www.transfermarkt.com/fc-stade-rennes/startseite/verein/273",
    # "https://www.transfermarkt.com/fc-toulouse/startseite/verein/415",
    # "https://www.transfermarkt.com/montpellier-hsc/startseite/verein/969",
    # "https://www.transfermarkt.com/rc-strassburg-alsace/startseite/verein/667",
    # "https://www.transfermarkt.com/fc-nantes/startseite/verein/995",
    # "https://www.transfermarkt.com/ac-le-havre/startseite/verein/738",
    # "https://www.transfermarkt.com/aj-auxerre/startseite/verein/290",
    # "https://www.transfermarkt.com/sco-angers/startseite/verein/1420",
    # "https://www.transfermarkt.com/as-saint-etienne/startseite/verein/618"


    # Eredivisie teams links
    # "https://www.transfermarkt.com/ajax-amsterdam/startseite/verein/610",
    # "https://www.transfermarkt.com/almere-city-fc/startseite/verein/723",
    # "https://www.transfermarkt.com/az-alkmaar/startseite/verein/1090",
    # "https://www.transfermarkt.com/feyenoord-rotterdam/startseite/verein/234",
    # "https://www.transfermarkt.com/fortuna-sittard/startseite/verein/385",
    # "https://www.transfermarkt.com/go-ahead-eagles-deventer/startseite/verein/1435",
    # "https://www.transfermarkt.com/fc-groningen/startseite/verein/202",
    # "https://www.transfermarkt.com/sc-heerenveen/startseite/verein/306",
    # "https://www.transfermarkt.com/heracles-almelo/startseite/verein/1304",
    # "https://www.transfermarkt.com/nac-breda/startseite/verein/132",
    # "https://www.transfermarkt.com/nec-nijmegen/startseite/verein/467",
    # "https://www.transfermarkt.com/pec-zwolle/startseite/verein/1269",
    # "https://www.transfermarkt.com/psv-eindhoven/startseite/verein/383",
    # "https://www.transfermarkt.com/rkc-waalwijk/startseite/verein/235",
    # "https://www.transfermarkt.com/sparta-rotterdam/startseite/verein/468",
    # "https://www.transfermarkt.com/fc-twente-enschede/startseite/verein/317",
    # "https://www.transfermarkt.com/fc-utrecht/startseite/verein/200",
    # "https://www.transfermarkt.com/willem-ii-tilburg/startseite/verein/403"

    #Championship teams links
    # "https://www.transfermarkt.com/blackburn-rovers/startseite/verein/164",
    # "https://www.transfermarkt.com/bristol-city/startseite/verein/698",
    # "https://www.transfermarkt.com/cardiff-city/startseite/verein/603",
    # "https://www.transfermarkt.com/coventry-city/startseite/verein/990",
    # "https://www.transfermarkt.com/derby-county/startseite/verein/22",
    # "https://www.transfermarkt.com/hull-city/startseite/verein/3008",
    # "https://www.transfermarkt.com/leeds-united/startseite/verein/399",
    # "https://www.transfermarkt.com/fc-middlesbrough/startseite/verein/641",
    # "https://www.transfermarkt.com/fc-millwall/startseite/verein/1028",
    # "https://www.transfermarkt.com/norwich-city/startseite/verein/1123",
    # "https://www.transfermarkt.com/oxford-united/startseite/verein/988",
    # "https://www.transfermarkt.com/plymouth-argyle/startseite/verein/2262",
    # "https://www.transfermarkt.com/portsmouth-fc/startseite/verein/1020",
    # "https://www.transfermarkt.com/preston-north-end/startseite/verein/466",
    # "https://www.transfermarkt.com/queens-park-rangers/startseite/verein/1039",
    # "https://www.transfermarkt.com/sheffield-wednesday/startseite/verein/1035",
    # "https://www.transfermarkt.com/stoke-city/startseite/verein/512",
    # "https://www.transfermarkt.com/afc-sunderland/startseite/verein/289",
    # "https://www.transfermarkt.com/swansea-city/startseite/verein/2288",
    # "https://www.transfermarkt.com/fc-watford/startseite/verein/1010",
    # "https://www.transfermarkt.com/west-bromwich-albion/startseite/verein/984"
]



# HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}



def get_players_url(club_url):
    """Extracts player profile URLs from a club squad page in transfermarket"""
    players_url = []
    time.sleep(2)
    response = requests.get(club_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    players = soup.find_all(class_="hauptlink")

    for link in players:

        player_href = link.find('a')
        if isinstance(player_href, Tag):
            player_href = player_href.get("href")
            if "/profil/spieler/" in player_href:
                url = "https://www.transfermarkt.com" + player_href
                players_url.append(url)

    return players_url



def get_player_injury_details(url):
    """
    Extracts player injury information history
    Returns: A list of dictionaries containing injury details of a player for each season
    """
    all_injuries = []
    
    time.sleep(2)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Player Name
    player_name = ' '.join(soup.find("h1").text.split()[1:])

    # Find injury table
    table = soup.find("table", {"class": "items"})
    if table:
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            
            if len(cols) > 5:
                injury_dict = {  # Create a NEW dictionary for each row
                    'player_name': player_name,
                    'season': cols[0].text.strip(),
                    'injury': cols[1].text.strip(),
                    'from_date': cols[2].text.strip(),
                    'to_date': cols[3].text.strip(),
                    'days_out': cols[4].text.strip(),
                    'matches_missed': cols[5].text.strip()
                }

                all_injuries.append(injury_dict)
            
    
    return all_injuries



def get_player_details(url):
    """
    Extracts players details such as name, height, age/dob and position
    """

    time.sleep(2)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    my_list = ["height", "date of birth/age", "position"]

    details = {}

    # Extract player info table
    info_table = soup.find_all("div", {"class": "data-header__info-box"})
    
    for element in info_table:
        player_name = ' '.join(soup.find("h1").text.split()[1:])
        details['player_name'] = player_name
        for i in element.find_all("li"):
            parsed_data = i.text.strip().replace(",", "").replace("\n", "").split(":")
            if parsed_data[0].casefold() in my_list:
                details[parsed_data[0].casefold().replace(' ', "_")] = parsed_data[-1].strip()

    return details



def get_player_stats_url(club_url):
    """
    Extracts player profile URLs from a club squad page and constructs the stats link for player
    Returns: A list of player season stats URL
    """
    players_url = []
    time.sleep(2)
    response = requests.get(club_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    players = soup.find_all(class_="hauptlink")
    # print(players)

    for link in players:

        player_href = link.find('a')
        if isinstance(player_href, Tag):
            player_href = player_href.get("href")
            if "/profil/spieler/" in player_href:
                stats_href = player_href.replace("/profil/spieler/", '/leistungsdaten/spieler/')
                url = "https://www.transfermarkt.com" + stats_href
                players_url.append(url)

    return players_url



def get_minutes_played(url, max_retries=3):
    """
    Scrape player performance stats from Transfermarkt with retry on failure.
    Returns: Minutes played each season for a player
    """

    for attempt in range(max_retries):
        try:
            time.sleep(random.uniform(3, 6))  # Prevent rate-limiting

            # Send the request with a timeout
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()  # Raise error for 4xx/5xx status codes

            soup = BeautifulSoup(response.text, "html.parser")

            Player_match_minutes = {}

            # Extract Player Name
            player_name = ' '.join(soup.find("h1").text.split()[1:])

            # Find performance table
            table = soup.find_all("div", {"class": "box"})

            competition_list = []
            minutes_played = []

            if table:
                try:
                    season = table[1].find('h2').text.strip().split()[1]

                    competitions = table[1].find_all('td', class_='no-border-links')
                    for comp in competitions:
                        competition_list.append(comp.text)

                    try:
                        play_time = table[1].find_all('td', class_='rechts')[1].text.strip("'").replace(".", "")
                        minutes_played.append(int(play_time))
                    except ValueError:
                        pass

                    for item in table[2:-3]:
                        try:
                            table_header = item.find('a').text.strip()
                            if table_header not in competition_list:
                                for row in item.find_all('tr')[1:]:
                                    cols = row.find_all('td')
                                    if len(cols) > 8:
                                        other_comps_minutes = cols[-1].text.strip().replace("'", "")
                                        try:
                                            minutes_played.append(int(other_comps_minutes))
                                        except ValueError:
                                            pass

                                    Player_match_minutes['player_name'] = player_name
                                    Player_match_minutes['minutes_played'] = sum(minutes_played)
                                    Player_match_minutes['season'] = season
                        except AttributeError:
                            pass
                except IndexError:
                    pass

            return Player_match_minutes  # Return the extracted data if successful

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5)  # Wait before retrying

    print("Max retries reached. Skipping URL:", url)
    # Player_match_minutes['player_name'] = player_name
    # Player_match_minutes['minutes_played'] = "failed"
    # Player_match_minutes['season'] = season
    return {
        "player_name": "failed",
        "minutes_played": "failed",
        "season": "failed"
    }  # Return failed if all retries fail



years = ['2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014']


def scrape_player_minutes(club_urls, years: list, filename):
    """
    Scrapes player minutes by season from provided club URLs and appends to (or creates) a base CSV file.
    """
    # Check if CSV exists, else start with empty DataFrame
    if os.path.exists(filename):
        base_mins_df = pd.read_csv(filename)
    else:
        base_mins_df = pd.DataFrame()

    mins_list = []

    for url in club_urls:
        player_urls = get_player_stats_url(url)

        for stats_url in player_urls:
            print(f"Starting process for... {stats_url}")
            for year in years:
                full_url = f"{stats_url}/plus/0?saison={year}"
                player_minutes = get_minutes_played(full_url)
                mins_list.append(player_minutes)

        # Append new data to base DataFrame
        new_df = pd.DataFrame(mins_list)
        base_mins_df = pd.concat([base_mins_df, new_df], ignore_index=True)

    # Drop duplicates and save to file
    base_mins_df = base_mins_df.drop_duplicates()
    base_mins_df.to_csv(filename, index=False)
    print("Finished scraping minutes.")




def scrape_player_profiles(club_urls, filename):
    """
    Scrapes player profile information from each club and saves to a CSV.
    """
    base_df = pd.DataFrame()
    count = 0
    all_players = []

    for club_url in club_urls:
        print(f"Starting process for... {club_url}")
        players_urls = get_players_url(club_url)

        for url in players_urls:
            print(f"Getting details for... {url}")
            player_details = get_player_details(url)
            all_players.append(player_details)
            count += 1

            if count % 2 == 0:
                time.sleep(2)

        df = pd.DataFrame(all_players)
        base_df = pd.concat([base_df, df], ignore_index=True)

    base_df = base_df.drop_duplicates()
    base_df.to_csv(filename, index=False)
    print("Finished scraping player profiles.")



def scrape_injury_data(club_urls, filename):
    """
    Scrapes injury records for all players in the provided clubs and saves to a CSV.
    """
    base_injury_df = pd.DataFrame()

    for club_url in club_urls:
        print(f"Starting process for... {club_url}")
        player_urls = get_players_url(club_url)
        time.sleep(2)

        player_injuries = []

        for url in player_urls:
            print(f"Getting injury record for... {url}")
            player_id = url.split("/")[-1]
            injury_url = f"https://www.transfermarkt.com/spieler/verletzungen/spieler/{player_id}"
            player_injuries.append(get_player_injury_details(injury_url))

        flattened_injury_data = [item for sublist in player_injuries for item in sublist]
        injury_df = pd.DataFrame(flattened_injury_data)
        base_injury_df = pd.concat([base_injury_df, injury_df], ignore_index=True)

    base_injury_df = base_injury_df.drop_duplicates()
    base_injury_df.to_csv(filename, index=False)
    print("Finished scraping injury data.")



def merge_league_data(players_file, injuries_file, performance_file, output_file):
    """
    Reads and merges player, injury, and performance data for a league.
    Calculates player's age at time of injury and saves the final merged dataset.

    Args:
        players_file (str): Path to the league's players CSV file.
        injuries_file (str): Path to the league's injury CSV file.
        performance_file (str): Path to the league's performance CSV file.
        output_file (str): Path to save the final merged CSV dataset.
    """
    # Load datasets
    players_df = pd.read_csv(players_file)
    injuries_df = pd.read_csv(injuries_file)
    perf_df = pd.read_csv(performance_file)

    # Parse injury dates and extract injury year
    injuries_df['from_date'] = injuries_df['from_date'].str.strip()
    injuries_df['from_date'] = pd.to_datetime(injuries_df['from_date'], errors='coerce')
    injuries_df['injury_year'] = injuries_df['from_date'].dt.year.astype('Int32')

    # Extract current age from '(xx)' in 'date_of_birth/age'
    players_df['current_age'] = players_df['date_of_birth/age'].str.extract(r'\((\d+)\)').astype('Int32')

    # Merge to calculate age at time of injury
    injuries_df = injuries_df.merge(players_df[['player_name', 'current_age']], on='player_name', how='left')
    injuries_df['age_at_injury'] = injuries_df['current_age'] - (2025 - injuries_df['injury_year'])

    # Merge datasets together
    merged_df = players_df.merge(perf_df, on='player_name', how='left')
    full_merged = merged_df.merge(injuries_df, on=['player_name', 'season'], how='left')

    # Save final merged dataset
    full_merged.to_csv(output_file, index=False)
    print(f"Saved merged dataset to: {output_file}")


scrape_player_minutes(epl_club_urls, years, "test_data.csv")
# epl = pd.read_csv("epl_final_dataset.csv")
# la_liga = pd.read_csv("laliga_final_dataset.csv")
# bundesliga = pd.read_csv("bundesliga_final_dataset.csv")
# eredivisie = pd.read_csv("eredivisie_final_dataset.csv")
# championship = pd.read_csv("championship_final_dataset.csv")
# league_1 = pd.read_csv('league_1_final_dataset.csv')


