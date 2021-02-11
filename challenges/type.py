def main():
    entry=input('Make entry \n')
    try:
        int(entry)
        print(entry,' Is of integer type')
    except:
        print('is string of length: ',len(entry))

if __name__ == "__main__":
    main()