class CreateVisits < ActiveRecord::Migration
  def change
    create_table :visits do |t|
      t.string :url
      t.datetime :visit_at

      t.timestamps
    end

    add_index :visits, :url
    add_index :visits, :visit_at
  end
end
