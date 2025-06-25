import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._currentCountry = None

    def handleCalcola(self, e):
        input = self._view._txtAnno.value
        try:
            year = int(input)
            if not (year >= 1816 and year <=2016):
                self._view._txt_result.controls.clear()
                self._view._txt_result.controls.append(ft.Text(f"Inserire un valore valido.",
                                                               color="red"))
                self._view.update_page()
                print(f"Inserire un valore valido.")
                return
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Inserire un valore valido.",
                                                               color="red"))
            self._view.update_page()
            print(f"Inserire un valore valido.")
            return
        self._model.buildGraph(year)
        self._view._btnRaggiungibili.disabled = False
        self.fillDDStato()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumComponentiConnesse()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito il dettaglio sui nodi:"))
        for c in self._model._graph.nodes():
            self._view._txt_result.controls.append(ft.Text(f"{c} - Vicini: {self._model.calcolaNumConfinanti(c)}"))
        self._view.update_page()


    def handleRaggiungibili(self, e):
        input = self._currentCountry
        if input is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Selezionare uno stato.",
                                                           color="red"))
            self._view.update_page()
            print(f"Selezionare uno stato.")
            return
        raggiungibili = self._model.calcolaRaggiungibiliRicorsivo(input)
        if len(raggiungibili) == 0:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Non ci sono stati raggiungibili da quello selezionato."))
            self._view.update_page()
            print(f"Non ci sono stati raggiungibili da quello selezionato.")
            return
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Di seguito gli stati raggiungibili:"))
        for c in raggiungibili:
            self._view._txt_result.controls.append(ft.Text(c))
        self._view.update_page()


    def fillDDStato(self):
        allCountries = self._model._allCountries
        for c in allCountries:
            self._view._ddStato.options.append(ft.dropdown.Option(text=c.StateNme,
                                                                  data=c,
                                                                  on_click=self.readDDStato))
        self._view.update_page()


    def readDDStato(self, e):
        print("readDDStato called ")
        if e.control.data is None:
            self._currentCountry = None
        else:
            self._currentCountry = e.control.data
        print(self._currentCountry)
