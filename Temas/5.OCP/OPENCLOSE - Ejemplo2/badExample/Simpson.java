package badExample;

public class Simpson {
    public static void hablar(Caricatura personaje){
        switch (personaje.name){
            case "Homero":
            System.out.println("Ou!");
            break;

            case "Bart":
            System.out.println("Caramba!");
            break;

            default:
                System.out.println("Personaje incorrecto");
        }
    }
}