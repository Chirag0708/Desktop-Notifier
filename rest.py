from plyer import notification
import time
if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** TAKE REST *** ",
            message="Rest is vital for better mental health, increased concentration and memory, a healthier immune system, reduced stress, and improved mood",
            timeout=5)
        time.sleep(60*60)