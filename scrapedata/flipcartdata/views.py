
from django.shortcuts import render,HttpResponse
from .models import Product
import requests
from bs4 import BeautifulSoup
# Create your views here.


def home(self):
    country="de"
    asin="1015"
    urllist=["https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi","https://www.flipkart.com/search?count=40&otracker=CLP_filters&p%5B%5D=facets.smart_tv%255B%255D%3DYes&p%5B%5D=facets.resolution%255B%255D%3DUltra%2BHD%2B%25284K%2529&sid=ckf%2Fczl&otracker=nmenu_sub_TVs%20and%20Appliances_0_Smart%20and%20Ultra%20HD&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Smart%20%26%20Ultra%20HD",
    "https://www.flipkart.com/all/~cs-c470e9d9f4c9893754e997d194ada9b9/pr?sid=ajy,buh&marketplace=FLIPKART&restrictLocale=true&fm=personalisedRecommendation%2FC6&iid=R%3Ab%3Bpt%3Ahp%3Buid%3A8bc7d8f8-097f-11ed-8e6d-413a8cd9e4e3%3B.cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B&ssid=5sqbi5z6bk0000001658467894614&otracker=hp_reco_Top%2BSelection_1_6.dealCard.OMU_cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B_5&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_1_NA_view-all_5&cid=cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B","https://www.flipkart.com/baby-care/baby-oral-care/pr?sid=kyh,ga0&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_Baby%20%26%20Kids_0_Baby%20Oral%20Care"]
    for i in urllist:
            
        response=requests.get(i)
        htlmlData=response.content
        responseSoup=BeautifulSoup(htlmlData,"html.parser")
        # print(responseSoup)
        ProductImage=[]
        ProductPrice=[]
        ProductTitle=[]
        ProductDetails=[]

        for data in responseSoup.find_all("div",attrs={"class":"_2kHMtA"}):
            title=data.find("div",attrs={"class":"_4rR01T"})
            titleString=title.string
            image=data.find("img",attrs={"class":"_396cs4 _3exPp9"})
            imagedata=image.get("src")
            price=data.find("div",attrs={"class":"_30jeq3 _1_WHN1"})
            priceData=price.string
            details=data.find("div",attrs={"class":"col col-7-12"})
            ProductDetails.append(details.text)
            ProductTitle.append(titleString)
            ProductImage.append(imagedata)
            ProductPrice.append(priceData)

            createData=Product.objects.create(Name=titleString,image=imagedata,Price=priceData,Details=details.text)
        # print(ProductTitle)
        # print(ProductImage)
        # print(ProductDetails)
        # print(ProductPrice)

    return HttpResponse("Sucessfully Added ")
