def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

if __name__ == "__main__":
    main(x=[1,2,3],y=[3,3,0], z=[4,4,4],q=[2,3,0], w=[3,1,0])
    print()

    main(**{'x':[1,2,3], 'y':[3,3,0]})