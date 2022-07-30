package com.otcg.decks;

import java.util.ArrayList;

public class DeckModel {
    private int id;
    private String deckName;
    private String deckTcg;
    private ArrayList deck = new ArrayList();

    public Object[] getInfo() {
        return new Object[]{id, deckName, deckTcg};
    }

    public int getId(){
        return id;
    }

    public String getDeckName(){
        return deckName;
    }

    public String getDeckTcg() {
        return deckTcg;
    }

    public ArrayList getCards() {
        return deck;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setDeckName(String deckName) {
        this.deckName = deckName;
    }

    public void setDeckTcg(String deckTcg) {
        this.deckTcg = deckTcg;
    }

    public void setDeck(ArrayList deck) {
        this.deck = deck;
    }
}
