package com.otcg.api.services;

import com.otcg.api.decks.DeckModel;

import java.io.*;

public class FileService {
    public static void uploadDeck(DeckModel deck) {

        try (
                OutputStream file = new FileOutputStream("decks.ser",true);
                OutputStream buffer = new BufferedOutputStream(file);
                ObjectOutput output = new ObjectOutputStream(buffer);
        ){
            output.writeObject(deck);
        }
        catch(IOException ex){
            System.out.println(String.format("Cannot perform output. %s", ex));
        }
    }
}

