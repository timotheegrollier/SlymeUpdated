from slyme import SlymeDriver
import time

def main():

    slyme = SlymeDriver(pfname='Default')
    time.sleep(2)
    slyme.select_latest_chat()
    time.sleep(2)
    

    while True:
        prompt = input('Input a prompt:  ')
        if prompt == '':
            break
        output = slyme.completion(prompt)
        print(output)

    slyme.end_session()

if __name__ == "__main__":
    main()
