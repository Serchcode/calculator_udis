"""Imports."""

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import requests
from dotenv import load_dotenv
import os

load_dotenv()


class MainView(View):
    """
    Main View.

    This view show the main of converter template
    """

    def get(self, request):
        """
        Get method.

        This metod get render template "main"
        """
        template_name = "main.html"
        return render(request, template_name)


class ConverterView(View):
    """
    Converter View.

    This view show the converter template
    """

    def get(self, request):
        """
        Get method.

        This metod get render template "main"
        """
        template_name = "converter.html"
        return render(request, template_name)

    def post(self, request):
        """
        Post method.

        This method receive two params date-start, date_end and consulting
        the information of udis and dollars between date range of two params
        in banxico's api with this information calculate the min, max and
        average values of udis and dollars
        """
        # make the request to banxico's api
        start_date = request.POST["trip-start"]
        end_date = request.POST["trip-end"]
        url = os.getenv("URL_BANXICO").format(
            start_date, end_date
        )
        headers = {
            "Bmx-Token": os.getenv("TOKEN_BANXICO")
        }
        req = requests.get(url, headers=headers)
        res = req.json()
        series = res["bmx"]["series"]
        for s in series:
            s["datos"] = ([] if 'datos' not in s else s["datos"])
            if s["idSerie"] == "SF60653":
                dollars = s["datos"]
            if s["idSerie"] == "SP68257":
                udis = s["datos"]
        # obtain data for dolars
        info_dollars = [
            {k: v for k, v in item_dolar.items() if k in "dato"}
            for item_dolar in dollars
        ]
        date_dollars = [
            {k: v for k, v in date_dolar.items() if k in "fecha"}
            for date_dolar in dollars
        ]
        labels_d = [d["fecha"] for d in date_dollars]
        data_d = [float(d["dato"]) for d in info_dollars]
        graph_d = [d["dato"] for d in info_dollars]
        d_max = (max(data_d) if len(data_d) > 1 else 0)
        d_min = (min(data_d) if len(data_d) > 1 else 0)
        d_average = ((sum(data_d) / len(data_d)) if len(data_d) > 1 else 0)
        # obtain data for udis
        info_udis = [
            {k: v for k, v in item_udis.items() if k in "dato"}
            for item_udis in udis
        ]
        date_udis = [
            {k: v for k, v in date_udis.items() if k in "fecha"}
            for date_udis in udis
        ]
        labels_u = [d["fecha"] for d in date_udis]
        data_u = [float(d["dato"]) for d in info_udis]
        graph_u = [d["dato"] for d in info_udis]
        u_max = (max(data_u) if len(data_u) > 1 else 0)
        u_min = (min(data_u) if len(data_u) > 1 else 0)
        u_average = ((sum(data_u)/len(data_u)) if len(data_u) > 1 else 0)
        # construct the context
        context = {}
        context["d_max"] = d_max
        context["d_min"] = d_min
        context["d_average"] = d_average
        context["dolares"] = dollars
        context["labels_d"] = labels_d
        context["graph_d"] = graph_d
        context["u_max"] = u_max
        context["u_min"] = u_min
        context["u_average"] = u_average
        context["labels_u"] = labels_u
        context["graph_u"] = graph_u
        context["udis"] = udis
        template_name = "converter.html"
        return render(request, template_name, context)


class TiieView(View):
    """
    Tiie View.

    This view show the Tiee template
    """

    def get(self, request):
        """
        Get method.

        This metod get render template "tiie"
        """
        template_name = "tiie.html"
        return render(request, template_name)

    def post(self, request):
        """
        Post method.

        This metod post make a request to baxico's api for consulting the
        value of tiie in their diferent values between interval of dates
        """
        start_date = request.POST["trip-start"]
        end_date = request.POST["trip-end"]
        url = os.getenv("URL_BANXICO").format(
            start_date, end_date
        )
        headers = {
            "Bmx-Token": os.getenv("TOKEN_BANXICO")
        }
        req = requests.get(url, headers=headers)
        res = req.json()
        series = res["bmx"]["series"]
        for s in series:
            s["datos"] = ([] if 'datos' not in s else s["datos"])
            if s["idSerie"] == "SF283":
                tiie28 = s["datos"]
            if s["idSerie"] == "SF17801":
                tiie91 = s["datos"]
            if s["idSerie"] == "SF221962":
                tiie182 = s["datos"]
        # info tiie28
        info_tiie28 = [
            {k: v for k, v in item_tiie28.items() if k in "dato"}
            for item_tiie28 in tiie28
        ]
        date_tiie28 = [
            {k: v for k, v in date_tiie28.items() if k in "fecha"}
            for date_tiie28 in tiie28
        ]
        labels_tiie28 = [d["fecha"] for d in date_tiie28]
        data_tiie28 = [float(d["dato"]) for d in info_tiie28]
        graph_tiie28 = [d["dato"] for d in info_tiie28]
        tiie28_max = (max(data_tiie28) if len(data_tiie28) > 0 else 0)
        # info_tiee91
        info_tiie91 = [
            {k: v for k, v in item_tiie91.items() if k in "dato"}
            for item_tiie91 in tiie91
        ]
        date_tiie91 = [
            {k: v for k, v in date_tiie91.items() if k in "fecha"}
            for date_tiie91 in tiie91
        ]
        labels_tiie91 = [d["fecha"] for d in date_tiie91]
        data_tiie91 = [float(d["dato"]) for d in info_tiie91]
        graph_tiie91 = [d["dato"] for d in info_tiie91]
        tiie91_max = (max(data_tiie91) if len(data_tiie91) > 0 else 0)
        # info_tiee182
        info_tiie182 = [
            {k: v for k, v in item_tiie182.items() if k in "dato"}
            for item_tiie182 in tiie182
        ]
        date_tiie182 = [
            {k: v for k, v in date_tiie182.items() if k in "fecha"}
            for date_tiie182 in tiie182
        ]
        labels_tiie182 = [d["fecha"] for d in date_tiie182]
        data_tiie182 = [float(d["dato"]) for d in info_tiie182]
        graph_tiie182 = [d["dato"] for d in info_tiie182]
        tiie182_max = (max(data_tiie182)if len(data_tiie182) > 0 else 0)
        # context
        context = {}
        context["tiie28_max"] = tiie28_max
        context["labels_tiie28"] = labels_tiie28
        context["graph_tiie28"] = graph_tiie28
        context["tiie28"] = tiie28
        context["tiie91_max"] = tiie91_max
        context["labels_tiie91"] = labels_tiie91
        context["graph_tiie91"] = graph_tiie91
        context["tiie91"] = tiie91
        context["tiie182_max"] = tiie182_max
        context["labels_tiie182"] = labels_tiie182
        context["graph_tiie182"] = graph_tiie182
        context["tiie182"] = tiie182
        template_name = "tiie.html"
        return render(request, template_name, context)
