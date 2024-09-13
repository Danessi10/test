import time
from brw import Browser

Browser.load_page(url='https://getgems.io/collection/EQAOQdwdw8kGftJCSFgOErM1mBjYPe4DBPq8-AhF6vr9si5N?utm_source=homepage&utm_medium=top_collections&utm_campaign=collection_overview&filter=%7B%22saleType%22%3A%22none%22%7D')
time.sleep(10)

js = """
content = document.querySelector('.Grid__grid');
lastItems = Array.from(content.children).slice(-15);
content.innerHTML = '';
lastItems.forEach(
    item => content.append(item)
)
"""

counter = 0

while True: 
    try:
        if counter >= 3:
            Browser.driver.execute_script(js)
            Browser.driver.execute_script(f"window.scrollBy(0, -700);")      
            counter = 0     
        else:
            Browser.driver.execute_script(f"window.scrollBy(0, 3000);") 
            counter += 1

        time.sleep(2)
    except:
        continue