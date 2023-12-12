import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from data_processing import transform_data, load_mongo,extract_ticker

def main():
    # call the extract function
    #extract_ticker()
    # call the transform function
    transform_data()
    # call the load function
    load_mongo()
    return True

### Run Layer ###

if __name__ == '__main__':
    main()
    print('Data has been extracted, transformed, saved in a json file and loaded into mongodb')