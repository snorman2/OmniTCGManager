package com.otcg.api.decks;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.HashMap;



@RestController
@Validated
public class DeckController {

	private DeckService deckService = new DeckService();

	@PostMapping("/create")
	public ResponseEntity<String> createDeck(@Valid @RequestBody DeckModel newDeck){
		String response = deckService.createDeck(newDeck);
		return new ResponseEntity(response, HttpStatus.OK);
	}

	@GetMapping("/deck")
	public ResponseEntity getDeck(@RequestParam(value = "id")  String id){

			DeckModel deck = deckService.getDeck(id);
			if (deck == null || !(deck instanceof DeckModel)){
				String message = String.format("No deck with id %s exists", id);
				return new ResponseEntity<String>(message, HttpStatus.NOT_FOUND);
			}
			return new ResponseEntity<DeckModel>(deck, HttpStatus.OK);
	}

	@PostMapping("/deck/update")
	public ResponseEntity<String> updateDeck(@Valid  @RequestBody DeckModel updatedDeck){

		Boolean isUpdated = deckService.updateDeck(updatedDeck);
		String tcg = updatedDeck.getDeckTcg();
		String id = updatedDeck.getId();

		if (!isUpdated){
			String message = String.format("There was a problem when updating the deck. Ensure the Id is valid, Tcg is the same, or that the cards are not the same. Id: %s Tcg: %s", id,tcg);
			return new ResponseEntity(message, HttpStatus.NOT_FOUND);
		} else {
			String message = "Deck updated successfully.";
			return new ResponseEntity(message, HttpStatus.OK);

		}
	}

	@GetMapping("/collection")
	public ResponseEntity<HashMap<String,DeckModel>> getCollection(){

		HashMap<String,DeckModel> collection = deckService.getCollection();
		return new ResponseEntity<HashMap<String,DeckModel>>(collection, HttpStatus.OK);
	}


	@DeleteMapping("/deck")
	public ResponseEntity<String> deleteDeck(@RequestParam(value = "id") String id){

	Boolean didDelete = deckService.deleteDeck(id);

	if (!didDelete){
		String message = "Invalid deck id";
		return new ResponseEntity<>(message, HttpStatus.NOT_FOUND);
	}
	String message = "Deck deleted successfully";
	return new ResponseEntity<>(message, HttpStatus.OK);
	}
}
