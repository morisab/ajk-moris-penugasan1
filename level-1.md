# ajk-moris-penugasan1

Mash Burnedead hidup di dunia di mana sihir adalah segalanya. Meskipun dia tidak memiliki kemampuan sihir, dia memiliki kekuatan fisik yang luar biasa. Misalkan Mash ingin membuat program Python untuk melacak latihan fisiknya dan menggunakan Git untuk mengelola versi programnya.

Pertama, Mash membuat repositori Git baru dan membuat branch. 
Selanjutnya dia menambahkan file `mashcise.py` ke branch `master`.

![image1](media/Screenshot%20(392).png)

Rupanya mash salah mengupload file python, akhirnya mash lebih memilih mengupload secara langsung filenya yang benar pada GitHub. 
```python
#mashcise

def record_exercise():
    return 0
def track_progress():
    return 0
```

![image2](media/Screenshot%20(395).png)

Setelah Mash menambahkan file baru di branch `master`, dia menyadari bahwa dia ingin mengambil perubahan terbaru dari branch `master` di GitHub. Dia melakukan ini dengan perintah git pull.

```bash
git pull
```

![image3](media/Screenshot%20(396).png)

Kemudian, dia membuat branch `development` dan menambahkan baris kode baru pada mashcise.py.

```bash
git checkout -b development
```

```python
#mashcise

def record_exercise(exercise_type, reps):
    return {"type": exercise_type, "reps": reps}

def track_progress(exercise_records):
    return progress
```

Kemudian dia melakukan commit dan push pada branch `development`.
```bash
git add .
git commit
git push origin development
```

![image4](media/Screenshot%20(397).png)

Selanjutnya yang dia lakukan adalah membuat branch `featureA`.

```bash
git checkout -b featureA
```

![image5](media/Screenshot%20(398).png)

Pada branch `featureA`, Mash menulis fungsi untuk mencatat latihan fisiknya.

```python
def record_exercise(exercise_type, reps):
    print(f"Recording exercise: {exercise_type}, {reps} reps")
    return {"type": exercise_type, "reps": reps}
```


![image6](media/Screenshot%20(399).png)

Setelah itu, dia melakukan commit dan push ke branch `featureA`.

Kemudian mash bingung terhadap fungsi track_progress(), akhirnya dia memutuskan untuk menghapusnya dulu pada branch `development`
```bash
git checkout development
```

Lalu commit dan push ke branch `development`.

Selanjutnya dia baru sadar lupa menghitung berapa sets yang dilakukannya untuk setiap olahraga, sehingga mash harus memperbaiki kodenya. Mash kembali ke branch `featureA` kemudian memperbaiki kodenya

```python
def record_exercise(exercise_type, sets, reps):
    print(f"Recording exercise: {exercise_type}, {sets} sets, {reps} reps")
    return {"type": exercise_type, "sets": sets, "reps": reps}
```

![image7](media/Screenshot%20(401).png)

Karena memakan kue sus isi krim, akhirnya Mash tau apa yang harus dia tulis pada fungsi untuk melacak perkembangan latihan fisiknya sehingga dia membuat branch `featureB`. Karena Mash takut ide ini segera hilang, maka kemudian dia menyimpan perubahan sebelumnya kedalam stash

Mula-mula dia melihat perubahan yang belum dicommit.
```bash
git diff
```

![image8](media/Screenshot%20(402).png)

Setelah memastikan memang ada perubahan, kemudian baru dia menggunakan stash

```bash
git stash save "wip in record_exercise"
```

![image9](media/Screenshot%20(403).png)

Kemudian dia membuat branch `featureB`

```bash
git checkout development
git checkout -b featureB
```

![image10](media/Screenshot%20(404).png)

Pada branch `featureB`, Mash menulis fungsi untuk melacak perkembangan latihan fisiknya, namun karena terlalu lama dia sudah lupa dengan idenya tadi sehingga Mash hanya menuliskan sebagai berikut.

```python
def track_progress(exercise_records):
    progress = {}
    return progress
```

Dia melakukan commit dan push ke branch `featureB`.

![image11](media/Screenshot%20(405).png)


Setelah itu, dia beralih ke branch `featureA` dan mengerjakan kembali progress nya yang sebelumnya disimpan di stash.

```bash
git checkout `featureA`
git stash list
git stash pop
```

Kemudian Mash melakukan commit dan push ke branch `featureA`.

Mash beralih ke branch `development` dan melakukan merge dari branch `featureA`.

```bash
git checkout development
git merge featureA --no-ff
```
Karena terdapat konflik, maka mash harus menyelesaikan konflik ini terlebih dahulu. Karena Mash ingin menerima **perubahan** dari `featureA` maka pada VS Code klik accept incoming change 

Setelah tidur siang, mash memperoleh ide untuk logika fungsi untuk melacak latihan fisiknya. Dia langsung mengeksekusi idenya ini.
```bash
git checkout featureB
```

```python
def track_progress(exercise_records):
    progress = {}
    total_sets = 0
    total_reps = 0
    for record in exercise_records:
        if record["type"] not in progress:
            progress[record["type"]] = {"sets": record["sets"], "reps": record["reps"]}
        else:
            progress[record["type"]]["sets"] += record["sets"]
            progress[record["type"]]["reps"] += record["reps"]
        total_sets += record["sets"]
        total_reps += record["reps"]
```

Kemudian dia melakukan commit dan push ke branch `featureB`
Mash juga kepikiran untuk menambahkan beberapa kode lain

```python
if total_reps == 0:
        return "You haven't done any reps yet!"
    elif total_reps < 0:
        return "Wait, how did you do negative reps?"
    else:
        return progress
```

Tapi karena Mash merasa kodenya ini ditertawakan oleh temannya, dia merasa malu kemudian. Tapi sebelumnya mash sudah terlanjut melakukan commit, akhrinya dia melakukan git reset untuk membatalkan commit terakhirnya.

```
git reset --hard HEAD~1
```

Kemudian beralih ke branch `development`. Mash menambahkan beberapa baris kode agar aplikasinya terlihat lebih interaktif.
```python
print("Welcome to Mashcise!")
print("Let's record your exercises.\n")

exercise_records = []
while True:
    exercise_type = input("Enter exercise type (or 'done' to finish): ")
    if exercise_type.lower() == 'done':
        break
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter number of reps per set: "))
    exercise_records.append(record_exercise(exercise_type, sets, reps))
```

Setelah mendapatkan ide untuk logika fungsi pelacakan latihan fisiknya, Mash memutuskan untuk menambahkan beberapa baris kode lagi di branch `featureB`:

```python
print("\nYour Progress:")
for exercise, data in progress.items():
    print(f"- {exercise}: {data['sets']} sets, {data['reps']} reps")
print(f"\nTotal: {total_sets} sets, {total_reps} reps")

return progress
```

Dia melakukan commit dan push perubahan ini ke branch `featureB`.

```bash
git add featureB.py
git commit -m "add function to display progress"
git push origin featureB
```

Setelah itu, Mash beralih ke branch `development` dan melakukan merge dari branch `featureB`.

```bash
git checkout development
git merge featureB --no-ff
```

Karena konfliknya terlalu banyak, maka pada VS Code pilih "Resolve in Merge Editor". Sesuaikan sesuai dengan bagaimana seharusnya kemudian commit dan push ke branch development.

Mash lupa untuk memanggil fungsi track_progress(), sehingga dia harus mengedit kode nya terlebih dahulu kemudian melakukan commit dan push lagi.
```python
print("\nRecording completed.\n")
track_progress(exercise_records)
```

Terakhir Mash melakukan merge dari branch `development` dan `master`

Akhirnya, Mash berhasil membuat program Python untuk melacak latihan fisiknya dengan bantuan Git. Mash berharap bahwa dengan adanya fungsi pelacakan ini, dia akan dapat melihat progres latihannya dengan lebih baik.