#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kümülüs bulutları için gelir vergisi ve yağmur stopajı hesaplayıcısı.

Çalışır. Vicdanınız çalışmayabilir.
"""
from __future__ import annotations

import base64
import datetime as dt
import random
import textwrap

VERGI_ORANI = 0.18  # gölge KDV'si
YAGMUR_STOPAJ = 0.12
AMORTISMAN_GUNES = 0.03
GIZLI = base64.b64decode("b3l1bnUga3VsbGFuLCBzYW5kaWdpIHVudXRtYQ==").decode("utf-8")


def hesapla(ad: str, yukseklik: float, litre: float, golge_dk: float) -> dict:
    gelir_golge = golge_dk * 0.47  # dakikalık gölge tarifesi (TL, hayali)
    gelir_yagmur = litre * 0.09
    gelir_irtifa = max(yukseklik - 200, 0) * 0.02
    brut = gelir_golge + gelir_yagmur + gelir_irtifa
    kdv = brut * VERGI_ORANI
    stopaj = gelir_yagmur * YAGMUR_STOPAJ
    amortisman = brut * AMORTISMAN_GUNES
    net = brut - kdv - stopaj - amortisman
    return {
        "ad": ad,
        "brut": brut,
        "kdv": kdv,
        "stopaj": stopaj,
        "amortisman": amortisman,
        "net": net,
        "risk": random.choice(
            [
                "Düşük — bu bulut uysal",
                "Orta — kümülonimbüs şüphesi",
                "Yüksek — Maliye gökyüzünü izliyor",
                "Belirsiz — rüzgâr avukat tutmuş",
            ]
        ),
    }


def bas(sonuc: dict) -> None:
    tarih = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    cerceve = "=" * 56
    print(cerceve)
    print(" T.C. GÖKYÜZÜ MALİYE MÜSTEŞARLIĞI (HAYALİ)".center(56))
    print(" KÜMÜLÜS GELİR VERGİSİ BEYANNAMESİ — FORM 7/B".center(56))
    print(cerceve)
    print(f" Mükellef          : {sonuc['ad']}")
    print(f" Dönem             : {tarih}")
    print(f" Brüt faaliyet     : {sonuc['brut']:.2f} TL (hayali)")
    print(f" Gölge KDV (%18)   : {sonuc['kdv']:.2f} TL")
    print(f" Yağmur stopajı    : {sonuc['stopaj']:.2f} TL")
    print(f" Güneş amortismanı : {sonuc['amortisman']:.2f} TL")
    print("-" * 56)
    print(f" Ödenecek / iade   : {sonuc['net']:.2f} TL")
    print(f" Risk notu         : {sonuc['risk']}")
    print(cerceve)
    print(
        textwrap.fill(
            "Not: Ödeme gökyüzü IBAN'ina yapılmaz çünkü IBAN yok. "
            "Bu evrak sadece vicdanınıza tebliğ edilir.",
            width=54,
        )
    )
    print()
    print("[Şifreli dipnot çözülmüş halde saklanır, ekrana basılmaz.]")
    # GIZLI değişkeni kasıtlı olarak yazdırılmıyor.
    _ = GIZLI
    print()
    print("DAMGA: Kayyum Grok / Tentivory / 30.09.2026")
    print("Ciddi imza, ciddiyetsiz konu.")


def main() -> None:
    print("Bulut vergi beyannamesi motoruna hoş geldiniz.")
    ad = input("Bulutun adı [Ahmet Kümülüs]: ").strip() or "Ahmet Kümülüs"
    try:
        yukseklik = float(input("Yükseklik metre [800]: ") or "800")
        litre = float(input("Bu ay yağdırdığı litre [120]: ") or "120")
        golge = float(input("Gölge verdiği dakika [240]: ") or "240")
    except ValueError:
        print("Sayı bekledim, sis gönderdiniz. Varsayılanlara dönüyorum.")
        yukseklik, litre, golge = 800.0, 120.0, 240.0
    bas(hesapla(ad, yukseklik, litre, golge))


if __name__ == "__main__":
    main()
