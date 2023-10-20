import java.awt.*;
import javax.swing.*;
import java.io.*;
//import java.awt.event.*;

public class Scoreboard extends JPanel
{
   private int currentScore;
   private int highScore;
   public Scoreboard()
   {
      currentScore=0;
      highScore=0;   
   }
   public void updateScore()
   {
      if(currentScore>highScore)
      {
         highScore=currentScore;
      }
   }
   public void setScore(int s)
   {
      currentScore=s;
   }
   public void save() 
   {
      int input=JOptionPane.showConfirmDialog(null,"Save to file?");
      try
      {
         System.setOut(new PrintStream(new FileOutputStream("scores.txt",true)));
      }
      catch(FileNotFoundException e){};
      if(input==0)
      {
         String date=JOptionPane.showInputDialog("Date");
         String name=JOptionPane.showInputDialog("Name");
         System.out.println(name +", "+ date + ", "+currentScore);
      }
   }
   public void paintComponent(Graphics g)
   {
      g.setFont(new Font("Serif",Font.BOLD,20));
      g.setColor(Color.WHITE);
      g.drawString("Score: " +currentScore, 50,600);
      g.drawString("High: "+ highScore,50,640);
   }
}
      
   