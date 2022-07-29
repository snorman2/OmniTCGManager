package com.otcg.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.*;


@SpringBootApplication
@RestController

public class OtcgManagerApplication {

	public static void main(String[] args) {
		SpringApplication.run(OtcgManagerApplication.class, args);
	}

	@PostMapping("/create")
	public String create(){
		return "new deck";
	}

	@GetMapping("/deck")
	public String getDeck(@RequestParam(value = "id", defaultValue = "0") String id){
		return String.format("Deck id is %s", id);
	}

	@GetMapping("/decks")
	public String getAllDecks(){
		return "decks";
	}



}
