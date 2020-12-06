# Shift
## Crypto [50 pts]
## Problème 
Nous travaillons depuis plusieurs mois sur le hack d'une application Java. Nos équipes sont bloquées car elle n'arrivent pas à trouver le bon mot de passe... Pouvez-vous nous aider à trouver quel est le mot de passe attendu par ce programme ?  
[Fichier attaché](files/1shift.java)
## Resolution
Dans le code source :
```java
import java.util.Scanner;

public class StrongAuthent {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Password please:");
        String str = sc.nextLine();
        if (shift(str).equals("136 138 172 134 144 130 154 160 182 230 232 228 96 220 206 190 198 228 242 224 232 96 186")){
            System.out.println("Welcome!");
        }
        else{
            System.out.println("Wrong password");
        }
    }
    static String shift(String pwd){
        String res = "";
        for (char ch: pwd.toCharArray()) {
            res += ((int) ch) * 2 + " ";
            System.out.println(res);
        }
        return res.trim();
    }
}

```
Au niveau de la ligne 8, nous pouvons voir une comparaison de la chaîne de retour de notre entrée après avoir été passée à une fonction appelée shift par rapport à une chaîne de nombres séparés par des espaces. La fonction de décalage prend simplement les valeurs décimales de chaque caractère de notre entrée, puis la multiplie par 2 et ajoute un espace à la fin. Cela signifie que nous pouvons récupérer la bonne entrée à partir de la chaîne des nombres séparés par un espace dans la ligne 8. Nous avons juste besoin de prendre chaque nombre et de le diviser par 2 puis de le convertir en ascii pour obtenir le flag. Ceci est la solution :  
```python
#!/usr/bin/python3

goal = "136 138 172 134 144 130 154 160 182 230 232 228 96 220 206 190 198 228 242 224 232 96 186"
print("".join([chr((int(_) // 2)) for _ in goal.split(" ")]))
```
