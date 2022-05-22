from selenium import webdriver
import time

#code by pythonjar, not me
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:\Windows/chromedriver.exe', chrome_options=chrome_options)


def scrap_fb(myurl,scroll_nbr):
    driver.get(myurl)
    #Scroll down N fois
    last_height = driver.execute_script("return document.body.scrollHeight")
    N = scroll_nbr
    k=0
    while k<N:
        k+=1
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    #

    #Lists of results
    dates=[]
    posts_texts=[]
    reactions_nbr=[]
    shares_nbr=[]
    comments_nbr=[]
    comments=[]
    post_images=[]
    post_videos=[]
    #
    k=1
    end_algo=False
    elt_path1 = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div['
    elt_path2 = ']'
    main_elt = driver.find_element_by_xpath(elt_path1+str(k)+elt_path2) 

    while(end_algo==False):
        #extract info from this post
        #Date
        try:
            pub_date = main_elt.find_elements_by_class_name('_5ptz')[0].text
            dates.append(pub_date)
        except:
            dates.append('')
        #post text
        try:
            texts = main_elt.find_elements_by_class_name('_5pbx')[0]
            post_text=''
            for pt in texts.find_elements_by_tag_name('p'):
                post_text = post_text + pt.text + ' '
                post_text = post_text.strip()
            posts_texts.append(post_text)
        except:
            posts_texts.append('')
        
        #get images or externe page urls
        img_ls=[]
        try:
            # get the image source
            imgs = main_elt.find_elements_by_class_name('scaledImageFitWidth')
            ind=1
            for img in imgs:
                src = img.get_attribute('src')
                img_ls.append(src)
                ind+=1
            post_images.append(str(img_ls))
        except:
            post_images.append([])
        #
        #get videos urls
        vid_ls=[]
        try:
            # get the image source
            vids = main_elt.find_elements_by_class_name('_ox1')
            ind=1
            for vid in vids:
                src = vid.get_attribute('src')
                vid_ls.append(src)
                ind+=1
            post_videos.append(str(vid_ls))
        except:
            post_videos.append([])
        #
        #reactions on post
        try:
            nbr_reactions = main_elt.find_elements_by_class_name('_81hb')[0]
            reactions_nbr.append(nbr_reactions.text)
        except:
            reactions_nbr.append('0')
        #nbr commentaires
        try:
            nbr_com = main_elt.find_elements_by_class_name('_4vn2')[0]
            nbr_com = nbr_com.find_element_by_tag_name('a').text
            comments_nbr.append(nbr_com)
        except:
            comments_nbr.append('0')
        #number of shares
        try:
            nbr_sh = main_elt.find_elements_by_class_name('_355t')[0].text
            shares_nbr.append(nbr_sh)
        except:
            shares_nbr.append('0')
        #select "all comments" option to show all comments of the post
        try:
            element = main_elt.find_element_by_class_name('_7a99')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            element = driver.find_elements_by_class_name('_54nc')[2]
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            #click to show more comments
            element = main_elt.find_element_by_class_name('_4sxc')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        except:
            print('No comments')
        #commentaires
        dict_com={}
        try:
            com=main_elt.find_elements_by_xpath("//div[@class='_72vr']")
            for x in com:
                try:
                    a = x.find_elements_by_xpath(".//a[@class='_6qw4']")
                    com_owner=a[0].get_attribute("href")
                    com_text= x.text
                    dict_com[com_owner]=com_text
                except:
                    continue
            comments.append(str(dict_com))
        except:
            comments.append('')
        
        #Select the next post if it exists
        print('k = ',k)
        k+=1
        try:
            main_elt = driver.find_element_by_xpath(elt_path1+str(k)+elt_path2)
            elt_cla = main_elt.get_attribute("class")
            if elt_cla == '_4-u2 _4-u8':
                pass
            elif elt_cla == '_1xnd':
                elt_path1 += str(k)+']/div['
                k=1
                main_elt = driver.find_element_by_xpath(elt_path1+str(k)+elt_path2)
            else:
                end_algo=True
                #break
            
        except:
            end_algo=True
    driver.close()
    return dates,posts_texts,reactions_nbr,shares_nbr,comments_nbr,comments,post_images,post_videos

