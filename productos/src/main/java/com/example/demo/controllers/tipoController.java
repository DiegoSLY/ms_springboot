package com.example.demo.controllers;

import com.example.demo.models.productsModel;
import com.example.demo.models.tipoModel;
import com.example.demo.services.serviceTipo.tipoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class tipoController {

    @Autowired
    tipoService tService;

    @RequestMapping("/welcome")
    public String welcomepage() {
        return "Bienvenido a mi api";
    }

    @GetMapping(value = "/tipo", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<tipoModel> getAllTipo() {
        return tService.getAlltipo();
    }

    @GetMapping(value = "/tipo/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public tipoModel getProId(@PathVariable("id") int id) {
        return tService.gettipo(id);
    }

    @PostMapping(value = "/loadInBodega", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.TEXT_PLAIN_VALUE)
    public String loadTipo(@RequestBody tipoModel newTipo) {
        return String.valueOf(tService.createtipo(newTipo));
    }

    @PutMapping(value = "/updateTipo", consumes = MediaType.APPLICATION_JSON_VALUE)
    public void updateTipo(@RequestBody tipoModel tipoCreated) {
        tService.updatetipo(tipoCreated);
    }

    @DeleteMapping(value = "/delTipo/{id}")
    public void delTipo(@PathVariable("id") int idTipo) {
        tService.deltipo(idTipo);
    }

}
