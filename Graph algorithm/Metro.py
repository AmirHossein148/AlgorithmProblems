import heapq
from collections import defaultdict

line1 = 'Tajrish Gheytariyeh Shahid_Sadr Gholhak Doctor_Shariati Mirdamad Shahid_Haghani Shahid_Hemmat Mosalla-ye_Emam_Khomeini Shahid_Beheshti Shahid_Mofatteh Shohada-ye_Haftom-e_Tir Taleghani Darvazeh_Dowlat Sadi Emam_Khomeini Panzdah-e_Khordad Khayyam Meydan-e_Mohammadiyeh Shoush Payaneh_Jonoub Shahid_Bokharaei Ali_Abad Javanmard-e_Ghassab Shahr-e_Rey Palayeshgah Shahed-Bagher_Shahr Haram-e_Motahhar-e_Emam_Khomeini Kahrizak'
line2 = 'Farhangsara Tehranpars Shahid_Bagheri Daneshgah-e_Elm-o_Sanat Sarsabz Janbazan Fadak Sabalan Shahid_Madani Emam_Hossein Darvazeh_Shemiran Baharestan Mellat Emam_Khomeini Hasan_Abad Daneshgah-e_Emam_Ali Meydan-e_Hor Shahid_Navab-e_Safavi Shademan Daneshgah-e_Sharif Tarasht Tehran_Sadeghiyeh'
line3 = 'Ghaem Shahid_Mahallati Aghdasiyeh Nobonyad Hossein_Abad Meydan-e_Heravi Shahid_Zeynoddin Khajeh_Abdollah-e_Ansari Shahid_sayyad-e_Shirazi Shahid_Ghodousi Sohrevardi Shahid_Beheshti Mirza-ye_Shirazi Meydan-e_Jahad Meydan-e_Hazrat-e_Vali_Asr Teatr-e_Shahr Moniriyeh Mahdiyeh Rahahan Javadiyeh Zamzam Shahrak-e_Shariati Abdol_Abad Nemat_Abad Azadegan'
line4 = 'Shahid_Kolahdouz Nirou_Havaei Nabard Pirouzi Ebn-e_Sina Meydan-e_Shohada Darvazeh_Shemiran Darvazeh_Dowlat Ferdowsi Teatr-e_Shahr Meydan-e_Enghelab-e_Eslami Towhid Shademan Doctor_Habibollah Ostad_Moin Meydan-e_Azadi Bimeh Shahrk-e_Ekbatan Eram-e_Sabz'
line5 = 'Shahid_Sepahbod_Qasem_Soleimani Golshahr Mohammad_Shahr Karaj Atmosfer Garmdarreh Vardavard Iran_Khodro Chitgar Varzeshgah-e_Azadi Eram-e_Sabz Tehran_Sadeghiyeh'
line6 = 'Shahid_Sattari Shahid_Ashrafi_Esfahani Yadegar-e_Emam Marzdaran Shahrak-e_Azmayesh Daneshgah-e_Tarbiat_Modarres Meydan-e_Hazrat-e_Vali_Asr Shohada-ye_Haftom-e_Tir Emam_Hossein Meydan-e_Shohada Amir_Kabir Shahid_Rezaei Besat Kiyan_Shahr Dowlat_Abad'
line7 = 'Meydan-e_Sanat Borj-e_Milad-e_Tehran Boostan-e_Goftegou Daneshgah-e_Tarbiat_Modarres Modafean-e_Salamat Towhid Shahid_Navab-e_Safavi Roudaki Komeyl Beryanak Helal_Ahmar Mahdiyeh Meydan-e_Mohammadiyeh Mowlavi Meydan-e_Ghiyam Chehel_Tan-e_Doulab Ahang Basij'

metro = {
    1: list(line1.split()),
    2: list(line2.split()),
    3: list(line3.split()),
    4: list(line4.split()),
    5: list(line5.split()),
    6: list(line6.split()),
    7: list(line7.split()),
}


def build_graph(metro, stop_time=2, transfer_time=10):
    graph = {}
    station_to_lines = defaultdict(list)

    for line, stations in metro.items():
        for station in stations:
            graph[(station, line)] = []
            station_to_lines[station].append(line)

    transfer_stations = {station for station, lines in station_to_lines.items() if len(lines) > 1}

    for line, stations in metro.items():
        for i, station in enumerate(stations):
            if i + 1 < len(stations):
                neighbor = stations[i + 1]
                graph[(station, line)].append((stop_time, (neighbor, line)))
                graph[(neighbor, line)].append((stop_time, (station, line)))

            if station in transfer_stations:
                for other_line in station_to_lines[station]:
                    if other_line != line:
                        graph[(station, line)].append((transfer_time, (station, other_line)))
    return graph


def shortest_path(graph, metro, start, end):
    start_nodes = {
        (s, l) for l, stations in metro.items() for s in stations if s == start
    }
    end_nodes = {
        (s, l) for l, stations in metro.items() for s in stations if s == end
    }

    dist = {node: 10**18 for node in graph}
    for start in start_nodes:
        dist[start] = 0
        heap = [(0, 0, start)]  # (cost, counter, node) — counter avoids tuple comparison
        counter = 1

        while heap:
            cost, _, u = heapq.heappop(heap)
            if cost > dist[u]:
                continue
            if u in end_nodes:
                return cost
            for w, v in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, counter, v))
                    counter += 1

    return -1


graph = build_graph(metro)

n = int(input())
for _ in range(n):
    start, end = input().split()
    print(shortest_path(graph, metro, start, end)+29)