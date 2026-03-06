import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Temperature": [22, 24, 23, 25, 26, 27, 24]
}

df = pd.DataFrame(data)


print(df)


plt.figure()
plt.plot(df["Day"], df["Temperature"])
plt.xlabel("Days")
plt.ylabel("Temperature (C)")
plt.title("Temperature Variation Over a Week")
plt.show()
