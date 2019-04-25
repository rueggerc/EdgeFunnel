
def main():
    print("BEGIN")
    
    message = 'sensor3,64.04,99.90,1556182811311'
    print(f'message={message}')

    items = message.split(",")
    print(items)
    
    host = items[0]
    temperature = items[1]
    humidity = items[2]
    print(f"host={host} temp={temperature} humidity={humidity}")
    


if __name__ == '__main__':
    main()