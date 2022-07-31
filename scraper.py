import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# waktu kecepatan program
start_time = time.time()

df = pd.DataFrame(columns=["Title","Perusahaan","Lokasi","Gaji","Deskripsi"])


driver = webdriver.Edge()

# url website
link = "https://www.jobs.id/"

driver.get(link)

# search for job IT Support
driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[1]/div/input").send_keys("IT Support")
driver.find_element(By.XPATH,"/html/body/section[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/form/div[3]/div/button").click()

time.sleep(5)

results = driver.find_elements(By.XPATH,'//*[@id="job-ads-container"]/div')
print(results)
for result in results:
    title = result.find_element(By.XPATH,'.//h3').text
    perusahaan = result.find_element(By.XPATH,'.//p[1]/a').text
    if perusahaan.find("kota lainnya") != -1:
        perusahaan = "Perusahaan Rahasia"
    lokasi = result.find_element(By.XPATH,'.//p[1]/span[@class="location"]').text
    
    try:
        lokasilainnya = result.find_element(By.XPATH,'.//p[1]/a[@class="location-more"]').text
        lokasi = lokasi + " " + lokasilainnya
    except:
        pass
    gaji = result.find_element(By.XPATH,'.//p[2]').text
    deskripsi = result.find_element(By.XPATH,'.//p[3]').text
    deskripsi = deskripsi.removesuffix(' Tampilkan Semua')

    temp= []
    temp.append(title)
    temp.append(perusahaan)
    temp.append(lokasi)
    temp.append(gaji)
    temp.append(deskripsi)

    temp_series = pd.Series(temp,index=df.columns)
    df = df.append(temp_series,ignore_index=True)


# waktu kecepatan program
end_time = time.time()

# set index menjadi 1
df.index += 1 

df.to_csv('it_support.csv')

print("Program Execution Time: %s seconds" % (end_time - start_time))




