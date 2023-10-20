import java.awt.*;
import javax.swing.*;
import java.util.*;
import java.io.*;
public class Menu
{
   private Rectangle play=new Rectangle(Map.SIDE/2-50, Map.BOTTOM/2-25,100,50);
   private Rectangle score=new Rectangle(Map.SIDE/2-50, Map.BOTTOM/2-125,100,50);
   private Rectangle quit=new Rectangle(Map.SIDE/2-50, Map.BOTTOM/2-225,100,50);
   public void drawButtons(Graphics g)
   {
      g.setFont(new Font("Arial",Font.BOLD,50));
      g.setColor(Color.WHITE);
      g.drawString("My Game", Map.SIDE/2 -60, 50);
      g.drawString("STEVEN LI", 500,650);
      g.setFont(new Font("Arial",Font.BOLD,20));
      g.drawRect(Map.SIDE/2-50, Map.BOTTOM/2-25,100,50);
    //  g.draw(play);
      g.drawString("Start",Map.SIDE/2-40,Map.BOTTOM/2);
     // g.draw(score);
      g.drawRect(Map.SIDE/2-50, Map.BOTTOM/2-125,100,50);
      g.drawString("Load Scores", Map.SIDE/2-60,Map.BOTTOM/2-100);
     // g.draw(quit);
      g.drawRect(Map.SIDE/2-50, Map.BOTTOM/2-225,100,50);
      g.drawString("Quit",Map.SIDE/2-40,Map.BOTTOM/2-200);
   }
   public void getCredits()
   {
      Scanner scanner=null;
      String s=null;
      try
      {
         scanner=new Scanner(new File("scores.txt"));
         s=scanner.nextLine();
         while (scanner.hasNextLine())
         {
            s=s+"\n "+scanner.nextLine();
         }
         
      }
      catch(IOException e){}
      
      JOptionPane.showMessageDialog(null,s,"scores",JOptionPane.PLAIN_MESSAGE);

   //  }
    // catch(BadLocationException e){}
  }

  /* private class Listener extends MouseAdapter
   {
      public void mouseClicked(MouseEvent e)
      {
         if(Map.getState()==GameState.MENU)
         {
            int x=e.getX();
            int y=e.getY();
            if(x>Map.SIDE/2-50 && x<Map.SIDE/2+50)
            {
               if( y>Map.BOTTOM/2-25 && y<Map.BOTTOM/2+25)
               {
                  Map.setState(GameState.GAME);
               }
               
               
            }
         }
      }
   }*/
}