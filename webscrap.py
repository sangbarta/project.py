import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="enter the number of pages to parse",type=int)
parser.add_argument("--dbname", help="enter the number of pages to parse",type=int)
args = parser.parse_args()


oyo_url = "https://www.oyorooms.com/hotels-in-kolkata/?page-"
page_num_MAX = args.page_num_max
scraped_info_list =[]
connect.connect(args.dbname)

 for page_num in range(1, page_num_MAX):
    req = requests.get(oyo_url)
    content = req.content

    soup = BeautifulSoup(content,"html.parser")

    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})



  for hotel in all_hotels:
     hotel_dict = ()
     hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription_hotelName"}).text
     hotel_dict["adress"] = hotel.find("span",{"itemprop": "streetAdress"}).text
     hotel_dict["price"] = hotel.find("span",{"class":"listingPrice__finalPrice"}).text
     #try....except
     try:
      hotel_dict["rating"] = hotel.find("span", {"class":"hotelRating__ratingSummary"}).text
     except AttributeError:
      hotel_dict["rating"] = None


    parent_amenities_element = hotel.find("div",{"class":"amenitywrapper"})

    amenities_list = []
    for amenity in parent_amenities_element.find_all("div",{"class":"amenitywrapper"}):
        amenities_list.append(amenity.find("span",{"class": "d-body-smd-Ellipsis"}).text.strip())

    hotel_dict["amenities"]= ", ".join(amenities_list[:-1])

    scraped_info_list.append(hotel_dict)
    connect.insert_into_table(args.dbname, tuple(hotel_dict.values())


    #print(hotel_name, hotel_address, hotel_price, hotel_rating,amenities_list)
dataframe = pandas.DataFrame(scraped_info_list)
dataframe.to_csv("oyo.csv")
connect.get_hotel_info(args.dbname)
