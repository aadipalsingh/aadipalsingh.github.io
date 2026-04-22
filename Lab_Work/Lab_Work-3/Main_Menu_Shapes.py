import ThreeD_Shapes as ts

while True:
    print("\n----- 3D SHAPES MENU -----")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Exit")

    choice = int(input("Select a shape: "))

    if choice == 6:
        print("Exiting program...")
        break

    print("\n--- Select Operation ---")
    print("1. Curved Surface Area (CSA)")
    print("2. Total Surface Area (TSA)")
    print("3. Volume")

    op = int(input("Enter operation: "))

    # ---------------- CUBE ----------------
    if choice == 1:
        a = float(input("Enter side of cube: "))
        
        if op == 1:
            print("CSA =", ts.cube_csa(a))
        elif op == 2:
            print("TSA =", ts.cube_tsa(a))
        elif op == 3:
            print("Volume =", ts.cube_volume(a))

    # ---------------- CUBOID ----------------
    elif choice == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))
        
        if op == 1:
            print("CSA =", ts.cuboid_csa(l, b, h))
        elif op == 2:
            print("TSA =", ts.cuboid_tsa(l, b, h))
        elif op == 3:
            print("Volume =", ts.cuboid_volume(l, b, h))

    # ---------------- CYLINDER ----------------
    elif choice == 3:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        
        if op == 1:
            print("CSA =", ts.cylinder_csa(r, h))
        elif op == 2:
            print("TSA =", ts.cylinder_tsa(r, h))
        elif op == 3:
            print("Volume =", ts.cylinder_volume(r, h))

    # ---------------- CONE ----------------
    elif choice == 4:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        l = float(input("Enter slant height: "))
        
        if op == 1:
            print("CSA =", ts.cone_csa(r, l))
        elif op == 2:
            print("TSA =", ts.cone_tsa(r, l))
        elif op == 3:
            print("Volume =", ts.cone_volume(r, h))

    # ---------------- SPHERE ----------------
    elif choice == 5:
        r = float(input("Enter radius: "))
        
        if op == 1:
            print("CSA =", ts.sphere_csa(r))
        elif op == 2:
            print("TSA =", ts.sphere_tsa(r))
        elif op == 3:
            print("Volume =", ts.sphere_volume(r))

    else:
        print("Invalid shape choice!")
