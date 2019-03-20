body = driver.find_element_by_css_selector('body')

        Y = 0
        while True:
            if Y == 0:
                Y = driver.execute_script('return window.scrollY')
            else:
                tmp = driver.execute_script('return window.scrollY')
                print(" Y값 : ", Y)
                print(" tmp값 : ", tmp)
                if Y == tmp:
                    idx += 1
                    if idx == 3:
                        break
                else:
                    Y = tmp
                    idx = 1

            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(SCROLL_PAUSE_TIME)
